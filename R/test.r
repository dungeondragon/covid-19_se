#!/usr/bin/env Rscript

library(readxl)

data <- read_excel('covid19.xlsx', sheet='Antal per dag region', range=cell_cols("A:B"))

x <- data[1]
y <- data[2]

mx <- cbind(x,y)

#X11()
plot(Totalt_antal_fall ~ Statistikdatum, mx)
#Sys.sleep(15)

