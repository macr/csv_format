FROM python:3
RUN mkdir /code
WORKDIR /code
RUN useradd -m web
USER web
ADD requirements.txt /code/
RUN pip install  --user  -r /code/requirements.txt 
RUN pip install --user  -i https://test.pypi.org/simple/ lambdata-richmondtest 
ADD format_csv.py /code
ENTRYPOINT [ "python", "/code/format_csv.py" ]

