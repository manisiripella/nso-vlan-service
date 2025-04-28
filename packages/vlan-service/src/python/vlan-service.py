from ncs import Service

class Main(Service):
    def create(self, tctx, root, service, proplist):
        self.log.info(f"Creating VLAN {service.vlan_id} on device {service.device}")
        vlan_template = self.ncs.template.Template(service)
        vlan_template.apply('vlan-template', {
            'VLAN_ID': service.vlan_id,
            'DEVICE_NAME': service.device
        })
