// arrays
let groceries = ["apples", "milk", "cheese", "bread"];
groceries.push("coffee")
groceries.unshift("carrot")
groceries.splice(1, 1, "peas")
groceries.pop()
groceries.shift();
console.log(groceries)
groceries.splice(groceries.indexOf("cheese"), 1 )
console.log(groceries);
