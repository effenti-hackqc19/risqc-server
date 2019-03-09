FROM            python:3.6.4
EXPOSE          4004

# Home directory
ENV HOME        /home/app
WORKDIR         $HOME

# Copy files for installation
COPY            ./requirements.txt      $HOME/requirements.txt

# Install dependencies
USER            root
RUN             pip install \
                    --no-cache-dir \
                    --disable-pip-version-check \
                    -r requirements.txt

COPY            ./                      $HOME

ENV FLASK_APP   $HOME/app.py

# Run server
CMD             ["flask", "run", "--host=0.0.0.0", "--port=4004"]