import Building from './5-building';

const b = new Building(100);
console.log(b);

class TestBuilding extends Building {}

function testBuilding() {
  try {
    // Create an instance and use it to avoid side effects warning
    const instance = new TestBuilding(200);
    console.log(instance);
  } catch (err) {
    console.log(err);
  }
}

// Call the function to execute the test
testBuilding();
