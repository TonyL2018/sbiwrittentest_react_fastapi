# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV PORT=8000

WORKDIR /app/

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --dev

COPY . /app/

EXPOSE 8000

# CMD ["uvicorn", "--reload", "main:app"]
