# This image is based on Alpine Linux project.
FROM python

# Configure environment
ENV SHELL /bin/bash
ENV ALPHA_USER alpha
ENV ALPHA_UID 1000
ENV HOME /home/$ALPHA_USER

# Create user with UID=1000 and in the 'users' group
RUN useradd -m -s /bin/bash -N -u $ALPHA_UID $ALPHA_USER

USER $ALPHA_USER
RUN umask 002
USER root

COPY  requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Setup user home directory
RUN mkdir /home/$ALPHA_USER/.local
WORKDIR /home/$ALPHA_USER/work
RUN chown -R root /home/$ALPHA_USER/
