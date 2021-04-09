library(ggplot2)

# Load data
data <- read.csv("users.csv", header=TRUE)

# Barplot
p <- ggplot(data, aes(x = as.factor(dob.age))) +
  geom_bar(stat = "count", position = "stack", fill = "#FF6666") +
  labs(x = "Age",
       y = "Count")

png("counts_by_age.png", width = 800, height = 400)
print(p)
dev.off()