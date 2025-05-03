// config.js

const config = {
  // Base URL for your backend API or any services you're using
  apiUrl: 'https://api.yourbackendservice.com', // Replace with your actual backend URL

  // Weather API key (for weather alerts)
  weatherApiKey: 'YOUR_WEATHER_API_KEY', // Replace with your weather API key

  // Configuration for how alerts should work (e.g., thresholds for Critical, Warning)
  alertConfig: {
    criticalThreshold: 10, // Example threshold for critical alerts
    warningThreshold: 5,   // Example threshold for warning alerts
    alertExpiration: 24,   // Time in hours for how long an alert should be active
  },

  // Environment setting (production or development)
  environment: process.env.NODE_ENV || 'development', // defaults to 'development'

  // Log level for debugging (can be 'info', 'warn', 'error', or 'debug')
  logLevel: 'info',

  // Bluetooth settings (if applicable)
  bluetoothRange: 100,  // Example Bluetooth range in meters (customize as needed)

  // Whether the site is in "offline" mode or if it's connected to the internet
  offlineMode: false, // This could be useful if your app has an "offline" feature

  // Data privacy and security settings (for later customization)
  dataPrivacy: {
    termsOfServiceUrl: 'https://yourwebsite.com/terms', // Link to your Terms of Service
    privacyPolicyUrl: 'https://yourwebsite.com/privacy-policy', // Link to your Privacy Policy
  }
};

module.exports = config;
