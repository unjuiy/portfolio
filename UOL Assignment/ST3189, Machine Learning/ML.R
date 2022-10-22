### load libraries
library(ggplot2)
library(corrplot)
library(randomForest)
library(e1071)
library(corrplot)
library(caret)

### read data files
part1 = read.csv('EWCS_2016.csv')
part2 = read.csv('student-por.csv', sep = ';')
part3 = read.csv('bank.csv', sep = ';')

### ============= PART 1 ============= ###
### PCA model
pca_model <- prcomp(part1, scale = TRUE)
summary(pca_model)

## Scree plot
screeplot(pca_model, main = "", col = "green", type = "lines", pch = 1, npcs = length(pca_model$sdev))

## PC meanning
pca_model
# PC 1: Negative mean of variables excluding Q2a and Q2b
# PC 2: Average of Q90a, Q90b, Q90c, and Q90f
# PC 3: Negative mean of Q2a and Q2b
# PC 4: Q2a - Q2b
# PC 5: Negative number of Q90f
# PC 6: Average of Q87b and Q90b


## Biplot
biplot(pca_model)

## K-means Clustering (K=4)
pca_data = data.frame(pca_model$x[, 1:6])
kmeans_model = kmeans(pca_data, 4)
table(kmeans_model$cluster)
pca_data$cluster = kmeans_model$cluster
pca_data$cluster = factor(pca_data$cluster)

## Plotting by cluster
ggplot(pca_data, aes(x=PC1, y=PC2, color=cluster)) +
  geom_point()

rm(pca_data, pca_model, kmeans_model)

### ============= PART 2 ============= ###
### Data Preprocessing
# factor type
part2$school = factor(part2$school)
part2$sex = factor(part2$sex)
part2$address = factor(part2$address)
part2$famsize = factor(part2$famsize)
part2$Pstatus = factor(part2$Pstatus)
part2$Mjob = factor(part2$Mjob)
part2$Fjob = factor(part2$Fjob)
part2$reason = factor(part2$reason)
part2$guardian = factor(part2$guardian)
part2$schoolsup = factor(part2$schoolsup)
part2$famsup = factor(part2$famsup)
part2$paid = factor(part2$paid)
part2$activities = factor(part2$activities)
part2$nursery = factor(part2$nursery)
part2$higher = factor(part2$higher)
part2$internet = factor(part2$internet)
part2$romantic = factor(part2$romantic)

# summary
summary(part2)

# correlation between numeric variables
corrplot(cor(part2[,c(3,7,8,13,14,15,24:33)]),method = 'number')

# delete variable G1, G2
part2 = part2[, -c(31,32)]

### Train, Test 
train_idx <- sample(1:649, size = 454, replace=FALSE) # Total data * 0.7 = 454
train_data_p2 = part2[train_idx, ]
test_data_p2 = part2[-train_idx, ]

### Regression model Fitting
# (1) Linear regression
lm_model = lm(G3 ~ ., train_data_p2)
summary(lm_model)
# School, sex, Fedu, studytime, failures, schoolsup, higher, farmel, health
predicted = predict(lm_model, test_data_p2)
rsq <- function (x, y) cor(x, y) ^ 2
rsq(test_data_p2$G3,predicted)

# (2) Tree based regression (random Forest)
rf_model = randomForest(G3 ~ ., train_data_p2, ntree = 500)  # number of trees = 500
predicted = predict(rf_model, test_data_p2)
rsq(test_data_p2$G3,predicted)

# (3) Non-linear method (SVM)
svm_model = svm(G3 ~ ., train_data_p2, kernel = 'radial')
predicted = predict(svm_model, test_data_p2)
rsq(test_data_p2$G3,predicted)

rm(lm_model, rf_model, svm_model, train_idx, train_data_p2, test_data_p2, predicted, rsq)

### ============= PART 3 ============= ###
### Data Preprocessing
# factor type
part3$job = factor(part3$job)
part3$marital = factor(part3$marital)
part3$education = factor(part3$education)
part3$default = factor(part3$default)
part3$housing = factor(part3$housing)
part3$loan = factor(part3$loan)
part3$contact = factor(part3$contact)
part3$month = factor(part3$month)
part3$poutcome = factor(part3$poutcome)
part3$y = factor(part3$y)

# summary
summary(part3)
# y 값의 no가 yes보다 훨씬 많은 class imbalance 문제가 있음.

# correlation between numeric variables
corrplot(cor(part3[,c(1,6,10,12:15)]),method = 'number')


### Train, Test 
test_sample = c(sample(which(part3$y == 'no'), 100), sample(which(part3$y == 'yes'), 100))
train_data_p3 = part3[-test_sample, ]
test_data_p3 = part3[test_sample, ]

### To solve Class imbalance problem, oversampling
over_sampled_data = train_data_p3[sample(which(train_data_p3$y == 'yes'), 3900-421, replace = T), ]
train_data_p3 = rbind(train_data_p3, over_sampled_data)
summary(train_data_p3)


### Classification model Fitting
# (1) Logistic regression
glm_model = glm(y ~ ., train_data_p3, family = binomial)
predicted = predict(glm_model, test_data_p3, type = "response")
predicted = ifelse(predicted > 0.5, 'yes', 'no')
predicted = factor(predicted)
confusionMatrix(predicted, test_data_p3$y)
#Accuracy : 0.8
#Sensitivity : 0.85
#Specificity : 0.8

# (2) Tree based regression (random Forest)
rf_model = randomForest(y ~ ., train_data_p3, ntree = 500)
predicted = predict(rf_model, test_data_p3)
confusionMatrix(predicted, test_data_p3$y)
#Accuracy : 0.67
#Sensitivity : 0.95
#Specificity : 0.4

# (3) Non-linear method (SVM)
svm_model = svm(y ~ ., train_data_p3, kernel = 'radial')
predicted = predict(svm_model, test_data_p3)
confusionMatrix(predicted, test_data_p3$y)
#Accuracy : 0.8
#Sensitivity : 0.82
#Specificity : 0.79

rm(glm_model, rf_model, svm_model, train_data_p3, test_data_p3, test_sample, over_sampled_data, predicted)

