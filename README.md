## Frontend

Creating a Vue project with Vite
```
cd frontend
npm create vite@latest __app_name__
cd __app_name__
```

Add Tailwind 

- Follow Step 2 onwards [here](https://tailwindcss.com/docs/guides/vite#vue)
- Replace contents of style.css with the @tailwind directives

Component libraries

- [Flowbite Vue 3](https://flowbite-vue.com/)
- [Headless UI](https://headlessui.com/vue/menu)

Template libraries

- [Flowbite](https://flowbite.com/)
- [Tailwind Components](https://tailwindui.com/components)

Icons

- [Heroicon Vue](https://github.com/tailwindlabs/heroicons#vue)

Plugins

- [Prettier for Tailwind CSS](https://github.com/tailwindlabs/prettier-plugin-tailwindcss) (untested)
- [Prettier for VS Code](https://prettier.io/docs/en/editors.html)


## Backend
```
cd backend
touch requirements.txt
```

Create a virtual environment
```
pyenv virtualenv 3.10 __app_name__
pyenv local __app_name__
```

Install FastAPI

- Add `uvicorn[standard] fastapi` to `requirements.txt`

```
pip install -r requirements.txt
```

- Create a main.py file. Follow steps [here](https://fastapi.tiangolo.com/tutorial/first-steps/)
- Add CORS middleware. Folow steps [here](https://fastapi.tiangolo.com/tutorial/cors/)
