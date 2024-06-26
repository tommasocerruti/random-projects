## Project
This project is a simple todo app written in 'Next.js' (https://nextjs.org/) bootstrapped with 'create-next-app' (https://github.com/vercel/next.js/tree/canary/packages/create-next-app). 

## Creating the project

Created the project using 'npx create-next-app@latest .' and set everything to YES.

Installed all the dependencies with prisma using 'npm i prisma --save-dev', in order to interact with the db.

Initialised prisma settins sql-lite db using 'npx prisma init --datasource-provider sqlite', so this creates db schema under dir prisma.

Migrated to the db using 'npx prisma migrate dev --name init'

Created db.ts in order to use the db within the app.

Removed boilerplate in the global.css as well as in page.tsx, and modified layout.tsx.

Added another route, by creating a folder 'new' with inside its respective page.

Modified page.tsx to execute our intended behavior.

Created the folder component to create the TodoItem component.



## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
