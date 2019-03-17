FROM alpine:3.8
RUN apk add --update py3-zmq py3-pip protobuf openssh-client tcpdump
RUN pip3 install protobuf==3.6.1 tornado==5.1.1 flake8==3.6.0
RUN apk add iptables dnsmasq
ADD . /code
RUN flake8 /code/*.py
WORKDIR "/code"
RUN cp dnsmasq.conf /etc
CMD ["sh", "run.sh"]
