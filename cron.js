const cron = require('node-cron')
const sqlite3 = require('sqlite3');

function manageDB() {
    
var db = new sqlite3.Database('db.sqlite3');

 db.serialize(function() {
  // Create a table
//   db.run("CREATE TABLE IF NOT EXISTS Foo (id INTEGER PRIMARY KEY, name TEXT)")
  // Insert data into the table
//   db.run("INSERT INTO Foo (name) VALUES ('bar')");
  // Query data from the table
  // db.each("SELECT * from sklad_core_infobydate", function(err, row) {
  //   console.log(row);
  // });
  db.run("update sklad_core_product set quantity = left, left = 0, quantity_sold = 0, summ = 0 where product_id = 13");
  db.each("SELECT * from sklad_core_product", function(err, row) {
    console.log(row);
  }); 
});
 db.close();
}

cron.schedule('0 0 * * *', () => {
    manageDB();
});


