# Controls

## Control: Password Policy
- Description: Enforce strong passwords for all accounts.
- Implementation: Configure password policies on all systems.

## Control: Firewall
- Description: Implement a firewall to protect the network.
- Implementation: Use UFW to configure the firewall.

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```
