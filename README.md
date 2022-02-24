## Mac OS
Clone files and change directory
```
git clone https://github.com/hon3g/ds_api.git
cd ds_api
```
Run code
```
docker-compose up
```

## Example
POST 0.0.0.0:8000/api/v1/player/ <br/>
Request Body:
```
{
  "username": 'hong'
}
```
Returns <br/>
201 Created:
```
{
  "player_id": 1,
  "username": "hong",
  "xp": 0,
  "gold": 0
}
```
## TL;DR
```
docker-compose up
```
