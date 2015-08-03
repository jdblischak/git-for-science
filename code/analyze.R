#!/usr/bin/env Rscript

# Analyze peak size distribution across chromosomes.

data_dir <- "../data"
sites <- read.table(file.path(data_dir, "sites-union.bed"),
                    stringsAsFactors = FALSE)
colnames(sites) <- c("chr", "start", "end")

sites$chr <- factor(sites$chr, levels = paste0("chr", c(1:22, "X")))
sites$len <- sites$end - sites$start
sites_per_chr <- table(sites$chr)

pdf(file.path(data_dir, "sites-union.pdf"))
par(mfrow = c(3, 1))
hist(sites$len)
boxplot(len ~ chr, data = sites, las = 3)
barplot(sites_per_chr, las = 3)
dev.off()
