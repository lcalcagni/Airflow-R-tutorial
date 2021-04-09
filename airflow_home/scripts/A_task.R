library(httr)
library(jsonlite)

res = GET(
  url = "https://randomuser.me/api/",
  query = list(
    results=200,
    nat="ca",
    inc="gender,name,dob"
   )
)

data = fromJSON(content(res, "text"))

write.csv(data$results,"users.csv", row.names = FALSE, sep=",")