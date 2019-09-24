# Telegram Translation App

## Setting Up your Development Environment
- (Optional) Create a virtual environment to work in with
`python -m venv .env` and activate it with `source .env/bin/activate`
- Install the project's dependencies with `pip install -r requirements.txt`
- Generate a Telegram API key and hash [here](https://my.telegram.org/apps), and export them to your environment either manually or through a `secrets.sh` file
- Run the app with `python app`
- Quit the app with `^C`

## Running in docker

- [ ] Move this section to the wiki!

You need to create a my_account.session file by setting up the dev environment using the instructions above. 

Docker TODO: add ability to pass in api id / hash from docker CMD.

To install docker / docker-compose on ubuntu 18.04 do

```bash
sudo apt install -y docker docker-compose
```

Then to start the app in docker do
```
sudo docker-compose up -d
```

To stop the app do
```
sudo docker-compose down
```

### Setting up docker
To not have to run in sudo, you have to setup docker with a group id.

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker 
```

Then verify docker is installed iwth

```bash
docker run hello-world
```