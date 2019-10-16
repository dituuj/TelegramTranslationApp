## Telegram Translation App

### Setting Up your Development Environment
- (Optional) Create a virtual environment to work in with
`python -m venv .env` and activate it with `source .env/bin/activate`
- Install the project's dependencies with `pip install -r requirements.txt`
- Generate a Telegram API key and hash [here](https://my.telegram.org/apps), and export them to your environment either manually or through a `secrets.sh` file
- Run the app with `python app`
- Quit the app with `^C`


## Vagrant setup

1. install virtual box https://www.virtualbox.org/wiki/Downloads
2. install vagrant https://www.vagrantup.com/downloads.html


To start the box run

```bash
vagrant up
```

### Using vagrant

To enter the box

```bash
vagrant ssh
```

This will bring you into a vagrant shell.

The folder you ran `vagrant up` in will be mounted inside vagrant in the directory `/vagrant`. 

Do

```bash
cd vagrant
```






### Shutting down vagrant
When you're done with the VM: 
To close the box

```bash
vagrant destroy
```
