import HolbertonCourse from './2-hbtn_course';

const c1 = new HolbertonCourse('ES6', 1, ['Bob', 'Jane']);
console.log(c1.name);
c1.name = 'Python 101';
console.log(c1);

try {
  c1.name = 12; // This should throw an error if the setter validates type
} catch (err) {
  console.log(err); // Log the error if any occurs
}

try {
  // Directly check the constructor without using `new` for side effects
  // You might want to wrap this in a function or another testing mechanism
  (() => new HolbertonCourse('ES6', '1', ['Bob', 'Jane']))();
} catch (err) {
  console.log(err); // Log the error if any occurs
}
