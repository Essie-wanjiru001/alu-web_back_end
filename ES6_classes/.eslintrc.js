module.exports = {
  env: {
    browser: false,
    es6: true,
    jest: true,
  },
  extends: [
    'airbnb-base',
    'plugin:jest/all',
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
    'import/extensions': ['error', 'never', {
      js: 'never',
      jsx: 'never',
      ts: 'never',
      tsx: 'never',
    }],
    'jest/require-hook': 'off',
    'jest/no-conditional-expect': 'off',

  },
  overrides: [
    {
      files: ['*.js'],
      excludedFiles: 'babel.config.js',
      rules: {
        'jest/require-hook': 'off',
      },
    },
    {
      files: ['*.test.js', '*.spec.js'],
      rules: {
        'jest/require-hook': 'error',
      },
    },
  ],
};
