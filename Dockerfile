FROM jrei/systemd-debian:12

RUN apt update && apt install -y sudo wget procps curl systemd iproute2 python3 python3-pip iptables && rm -rf /var/lib/apt/lists/*
RUN curl -sL https://raw.githubusercontent.com/NL-TCH/raspap-webgui/REST-API/installers/raspbian.sh | bash -s -- --yes --wireguard 1 --openvpn 1 --adblock 1 --restapi 1

COPY firewall-rules.sh /home/firewall-rules.sh
RUN chmod +x /home/firewall-rules.sh

EXPOSE 8081

CMD [ "/bin/bash", "-c", "/home/firewall-rules.sh && /lib/systemd/systemd" ]