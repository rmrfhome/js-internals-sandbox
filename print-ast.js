const fs = require("fs");
const util = require('util');
const ast = require('abstract-syntax-tree');

const source = fs.readFileSync('functions.js', "utf8");
const tree = ast.parse(source);
console.log(util.inspect(tree, false, null, true));