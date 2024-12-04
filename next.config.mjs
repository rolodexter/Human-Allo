import nextra from 'nextra'

const withNextra = nextra({
  theme: 'nextra-theme-docs',
  themeConfig: './theme.config.tsx'
})

export default {
  ...withNextra(),
  output: 'export',
  basePath: process.env.GITHUB_ACTIONS ? '/Human-Allo' : '',
  assetPrefix: process.env.GITHUB_ACTIONS ? '/Human-Allo/' : ''
}