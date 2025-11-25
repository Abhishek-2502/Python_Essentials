# Deploying a Flask Project on Vercel

This guide provides step-by-step instructions to deploy a Flask project on Vercel. Follow these steps to get your Flask application up and running on Vercel.

## Prerequisites
- Python and Flask installed
- Vercel account
- GitHub account
- A Flask project ready for deployment

## Steps

### 1. Create `requirements.txt`
Generate a `requirements.txt` file containing all the dependencies required by your project.

## 2. Create vercel.json
```json
{
  "version": 2,
  "builds": [
    { "src": "app.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "(.*)", "dest": "app.py" }
  ]
}
```
> Note: Change the `app.py` according to the path of your `main file` file.

### 3. Push to GitHub
Create a repository on GitHub and push your project to the repository. 

### 4. Deploy on Vercel
1. Go to [Vercel](https://vercel.com/) and log in with your GitHub account.
2. Click on "Add New" then "Project".
3. Select your GitHub repository.
4. Name your deployment and configure your project settings if needed (such as the root directory).
5. Select framework as `Flask`.
5. Click "Deploy".

## Conclusion
After following these steps, your Flask project should be successfully deployed on Vercel. Visit your Vercel dashboard to manage and view your project.

## Author
Abhishek Rajput
