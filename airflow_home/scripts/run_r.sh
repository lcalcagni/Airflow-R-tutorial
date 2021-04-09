#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)

setwd(dirname(args[1]))
source(args[1])