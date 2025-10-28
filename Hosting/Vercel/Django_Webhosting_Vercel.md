# Deploying a Django Project on Vercel

This guide provides step-by-step instructions to deploy a Django project on Vercel. Follow these steps to get your Django application up and running on Vercel.

## Prerequisites
- Python and Django installed
- Vercel account
- GitHub account
- A Django project ready for deployment

## Steps

### 1. Create `requirements.txt`
Generate a `requirements.txt` file containing all the dependencies required by your project.

```sh
pip freeze > requirements.txt
```

### 2. Create `build_files.sh`
Create a file named `build_files.sh` in the same directory as your `manage.py` file and add the following code:

```sh
# build_files.sh
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
```

### 3. Create `vercel.json`
Create a `vercel.json` file in the same directory as your `manage.py` file and add the following code:

```json
{
    "version": 2,
    "builds": [
        {
            "src": "DjangoWebScraping/wsgi.py",
            "use": "@vercel/python",
            "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
        },
        {
            "src": "build_files.sh",
            "use": "@vercel/static-build",
            "config": {
                "distDir": "staticfiles_build"
            }
        }
    ],
    "routes": [
        {
            "src": "/static/(.*)",
            "dest": "/static/$1"
        },
        {
            "src": "/(.*)",
            "dest": "DjangoWebScraping/wsgi.py"
        }
    ]
}
```
> Note: Change the `src` and `dest` according to the path of your `wsgi.py` file.

### 4. Modify `wsgi.py`
Add the following line at the end of your `wsgi.py` file:

```python
app = application
```

### 5. Modify `settings.py`
Make the following changes in your `settings.py` file:

```python
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', '.now.sh']
```

### 6. Push to GitHub
Create a repository on GitHub and push your project to the repository. You can create a new repository directly on [GitHub](https://github.com/) or use the command line.

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-URL>
git push -u origin main
```

### 7. Deploy on Vercel
1. Go to [Vercel](https://vercel.com/) and log in with your GitHub account.
2. Click on "Add New" then "Project".
3. Select your GitHub repository.
4. Name your deployment and configure your project settings if needed (such as the root directory).
5. Click "Deploy".

## Conclusion
After following these steps, your Django project should be successfully deployed on Vercel. Visit your Vercel dashboard to manage and view your project.

## Author
Abhishek Rajput
