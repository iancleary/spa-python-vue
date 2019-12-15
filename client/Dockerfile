# build stage
FROM node:lts as build-stage
# install yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | bash

# install and build add
WORKDIR /app
COPY package*.json ./
RUN yarn install
COPY . .
RUN yarn build

# production stage
FROM nginx:stable as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]