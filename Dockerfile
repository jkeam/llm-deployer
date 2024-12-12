FROM registry.access.redhat.com/ubi9/python-312:1-1733164709
USER root

# libs
RUN dnf install -y git-lfs

# transfer
USER 1001
RUN pip install boto3
COPY ./transfer.py .
CMD ["python", "./transfer.py"]
