# # Use the official Node.js base image
# FROM node:latest as builder

# Use the official Node.js
FROM node:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copying package.json and yarn.lock first to leverage Docker cache.
# This allows the dependency installation layer to be reused as long as
# package.json and yarn.lock do not change. This is a common practice to
# improve build efficiency, as dependencies change less frequently than source code.
COPY ./simple-api/package.json ./
COPY ./simple-api/yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the application source code
COPY ./simple-api .

# Expose the port the app runs on
EXPOSE 3000

# Start the application development mode
CMD [ "yarn", "run", "start" ]

# # Start the application watch mode
# CMD [ "yarn", "run", "start:dev" ]

# # Start the application production mode
# CMD [ "yarn", "run", "start:dev" ]