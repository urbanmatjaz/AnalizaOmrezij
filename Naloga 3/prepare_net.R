wdir = "C:/Users/Uporabnik/Desktop/Magisterij/Analiza omrežij/AnalizaOmrezij/Naloga 3"
setwd(wdir)
D <- read.csv("dict.csv",head=FALSE)
dim(D)
head(D)
source("https://raw.githubusercontent.com/bavla/Rnet/master/R/Pajek.R")
uvFac2net(factor(D$V1),factor(D$V2),Net="EngDict.net",twomode=TRUE)
