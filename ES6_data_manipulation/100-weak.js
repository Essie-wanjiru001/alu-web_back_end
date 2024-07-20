// 100-weak.js

// Export a const instance of WeakMap
export const weakMap = new WeakMap();

// Export a new function named queryAPI
export function queryAPI(endpoint) {
  // Check if the endpoint is already tracked in weakMap
  if (weakMap.has(endpoint)) {
    // Increment the count of queries for the endpoint
    const count = weakMap.get(endpoint) + 1;
    weakMap.set(endpoint, count);

    // Throw an error if the number of queries is >= 5
    if (count >= 5) {
      throw new Error('Endpoint load is high');
    }
  } else {
    // Initialize the count of queries for the endpoint
    weakMap.set(endpoint, 1);
  }
}
