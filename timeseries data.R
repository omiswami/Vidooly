new_data <- read.csv("https://raw.githubusercontent.com/vidoolytech/hiringtask/master/machine_learning/channel_stats/data/oct_march.csv", na.strings="F")
View(new_data)
child_1_views<-as.ts(new_data[1:148,'views'])
child_1_subscriber<-as.ts(new_data[1:148,'subscriber'])
child_1_videoscount<-as.ts(new_data[1:148,'videoscount'])
###checking mean trend over years
plot(child_1_views)
abline(reg = lm(child_1_views ~ time(child_1_views)))
###not station so transform
plot(log(child_1_views))

###converting dataset to stationary 
plot(diff(log(child_1_views)))      ##d=1
acf(diff(diff(log(child_1_views)))) ## q=0
pacf(diff(diff(log(child_1_views)))) ## p=5
fit <- arima(log(child_1_views), c(5, 1, 0), seasonal = list(order=c(5,1,0), frequency = 7))
pred<- predict(fit, n.ahead = 7*12)