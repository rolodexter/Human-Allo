const withNextra = require('nextra')({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.js'
})

const isProd = process.env.NODE_ENV === 'production'
module.exports = {
  ...withNextra(),
  basePath: isProd ? '/Human-Allo' : '',
  assetPrefix: isProd ? '/Human-Allo/' : ''
}