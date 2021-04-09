library(ggplot2)

# Load data
data <- read.csv("users.csv", header=TRUE)

# Barplot
p <- ggplot(data, aes(x = as.factor(gender), fill = gender)) +
  geom_bar(stat = "count", position = "stack") +
  labs(x = "Gender",
       y = "Count")

png("counts_by_gender.png")
print(p)
dev.off()