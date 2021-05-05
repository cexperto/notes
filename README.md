
# Notes Information System

Notes system simulation that consists of creating a system for registering academic grades to students, it is administered by teachers who are assigned several student groups



## Authors

- [@cexperto](https://www.github.com/cexperto)
- [@oscaremc](https://github.com/oscaremc)


  
## API Reference

#### Get all items teachers

```
https://notes-deploy-api.herokuapp.com/teachers

```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `teachers` | `string` | **optional**|

#### Get all courses

```
https://notes-deploy-api.herokuapp.com/courses

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| courses   | `string` | **optional** |

#### Get all students

```
https://notes-deploy-api.herokuapp.com/students

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| students   | `string` | **optional** |

#### Get all teachers and their groups

```
https://notes-deploy-api.herokuapp.com/tg

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| tg        | `string` | **optional**                       |
  

#### Get all teachers and groups of students

```
https://notes-deploy-api.herokuapp.com/tgs

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| tgs        | `string` | **optional**                       |
  

#### Get notes from specific course

```
https://notes-deploy-api.herokuapp.com/notes

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| id_c      | `integer` | **Required**                       |
  
#### Get notes from specific course

```
https://notes-deploy-api.herokuapp.com/updateNotes

```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
|updateNotes| `json`   | **Required**{ id,p1.p2,p3 }       |



## Deployment

To deploy this project run

```bash
  npm run deploy
```

  #### Frontend
  https://oscaremc.github.io/escuela/

  ### Backend
  https://notes-deploy-api.herokuapp.com/
## Installation 

this project is able in the 
https://oscaremc.github.io/escuela/

for view logic visit the git repo
https://github.com/cexperto/notes


    
## Tech Stack

**Client:** JavaScript, Html, css, git

**Server:** python, flask, gunicorn, psycopg2, postgresql, sql

  
