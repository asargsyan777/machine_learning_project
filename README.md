## Start Machine Learning project.

###Software and account Requiremet.

1. [Github Account](https://gihtub.com)
2. [Heroko Account](https://dashbord.heroko.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda envirement
```
conda create -p vev python==3.7 -y
```
```
conda activate venv/
```
OR
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add  <file_name>
```

To ignore  file or  folder from git we can write name of file/folder in .gitignore file

To check the git status
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information

1. HEROKU_EMAIL = annahay777@gmail.com
2. HEROKU_API_KEY = 
3. HEROKU_APP_NAME = ml-regression-apppp


BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .

>Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 94908541709e
```

To check running contaiers in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```

