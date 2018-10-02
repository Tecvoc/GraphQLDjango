const path = require('path');
var config = {
  mode: "development",
  entry: './frontend/entry.js',

  output: {
    path: path.resolve(__dirname, "static"),
    filename: 'index.js',
  },

  devServer: {
    inline: true,
    port: 8080
  },
  module: {
    rules: [{
        test: /\.jsx$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }, {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        },
      },
      {
        test: /\.css$/,
        exclude: /node_modules/,
        loaders: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(pdf|jpg|png|gif|svg|ico|png)$/,
        exclude: /node_modules/,
        use: [{
          loader: 'url-loader'
        }, ]
      }
    ]
  }
}

module.exports = config;
