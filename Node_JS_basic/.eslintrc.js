module.exports = {
  env: {
    browser: false,
    es6: true,
    // Do not include 'jest: true' globally
  },
  extends: [
    'airbnb-base',
    // Ensure 'plugin:jest/all' is applied only to test files
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module',
  },
  plugins: ['jest'],
  rules: {
    'max-classes-per-file': 'off',
    'no-underscore-dangle': 'off',
    'no-console': 'off',
    'no-shadow': 'off',
    'no-restricted-syntax': [
      'error',
      'LabeledStatement',
      'WithStatement',
    ],
    'jest/require-hook': 'off', // Disable Jest hooks globally if not needed
  },
  overrides: [
    {
      files: ['*.test.js', '*.spec.js'], // Apply Jest rules only to test files
      env: {
        jest: true,
      },
      extends: [
        'airbnb-base',
        'plugin:jest/all',
      ],
      rules: {
        // Jest-specific rules
        'jest/require-hook': 'error', // Ensure Jest hooks are required in test files
      },
    },
    {
      files: ['*.js'],
      excludedFiles: '*.test.js', // Exclude test files from general rules
    },
  ],
};
