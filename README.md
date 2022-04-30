
## Python-Automation Project

* Featching weather of a particular city using weather API
* Here we use python built-in modules such as requests.



## Features

- fetch the wether condition of a particular city
- we can also fetch maximum and minimum temperature
- fetch sunset and sunrise



## Tech used

**Languages used:** Python

**API:** openwetherAPI


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. 4b8e54bac7126f02b5732c4a7b936905 |

#### Get item

```http
  GET /api/items/${url}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `url`      | `string` | **Required**. https://api.openweathermap.org/data/2.5/weather |



