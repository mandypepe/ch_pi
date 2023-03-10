from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
CfnOutput
)
from aws_cdk import (aws_ec2 as ec2, aws_ecs as ecs,
                     aws_ecs_patterns as ecs_patterns)
from constructs import Construct
from aws_cdk.aws_ecr_assets import DockerImageAsset
# npx aws-cdk deploy --require-approval never
class InfraChStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "ch_pich", max_azs=3)  # default is all AZs in region
        """seg_name = ec2.SecurityGroup(self, 'ch_pich_security-group',
                                     vpc=vpc,
                                     allow_all_outbound=False,
                                     )
        seg_name.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description=f'ingress {80}',
        )
        seg_name.add_ingress_rule(
            peer=ec2.Peer.any_ipv6(),
            connection=ec2.Port.tcp(80),
            description=f'ingress {80}',
        )
        seg_name.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description=f'ingress {443}',
        )
        seg_name.add_ingress_rule(
            peer=ec2.Peer.any_ipv6(),
            connection=ec2.Port.tcp(443),
            description=f'ingress {443}',
        )
        seg_name.add_egress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.all_tcp(),
            description='egress any',
        )
        seg_name.add_egress_rule(
            peer=ec2.Peer.any_ipv6(),
            connection=ec2.Port.all_tcp(),
            description='egress any',
        )"""

        cluster = ecs.Cluster(self, "ch_pich_Cluster", vpc=vpc)


        appload=ecs_patterns.ApplicationLoadBalancedFargateService(self, "ch_pich_FargateService",
                                                           cluster=cluster,  # Required
                                                           cpu=512,  # Default is 256
                                                           desired_count=2,  # Default is 1
                                                           task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                                                                image=ecs.ContainerImage.from_asset(
                                                                    directory='srcdockerfiles'
                                                                ),
                                                           ),
                                                           memory_limit_mib=2048,  # Default is 512
                                                           public_load_balancer=True,
                                                                   assign_public_ip=True,

                                                           #security_groups=[seg_name]
                                                           )  # Default is True
        CfnOutput(self, "Load_balancer_dns_name", value=appload.load_balancer.load_balancer_dns_name)


