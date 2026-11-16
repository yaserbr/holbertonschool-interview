#!/usr/bin/node

const request = require('request');

const URL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
console.log(URL);

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const characters = JSON.parse(body).characters;
  const names = [];
  let counter = 0;

  for (let index = 0; index < characters.length; index++) {
    request(characters[index], (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      names[index] = JSON.parse(body).name;
      counter++;

      if (counter === characters.length) {
        names.forEach(name => console.log(name));
      }
    });
  }
});
