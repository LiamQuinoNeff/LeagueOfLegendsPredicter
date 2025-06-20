rm(list=ls(all=TRUE))
graphics.off()
cat("\014")

library(tidyverse)
library(ggplot2)
library(dplyr)
library(readr)

data_limpio_sin_outliers <- read_csv("Downloads/data_limpio_sin_outliers.csv") 

str(data_limpio_sin_outliers)

data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-blueWardsPlaced)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-blueWardsDestroyed)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-redWardsDestroyed)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-redWardsPlaced)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-blueHeralds)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-redHeralds)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-blueTotalJungleMinionsKilled)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-redTotalJungleMinionsKilled)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-blueFirstBlood)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-redFirstBlood)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-blueTotalMinionsKilled)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-redTotalMinionsKilled)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-blueDragons)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-redDragons)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-blueTotalExperience)
data_limpio_sin_outliers <- data_limpio_sin_outliers %>% select(-redTotalExperience)

summary(data_limpio_sin_outliers)
colnames(data_limpio_sin_outliers)

write.csv(data_limpio_sin_outliers, "data_normalizado_limpio.csv", row.names = FALSE)
