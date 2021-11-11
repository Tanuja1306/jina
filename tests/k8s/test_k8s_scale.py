import pytest

from jina import Flow

DEFAULT_REPLICAS = 2


@pytest.mark.timeout(3600)
@pytest.mark.parametrize('shards', [1])
def test_k8s_scale(k8s_cluster, load_images_in_kind, set_test_pip_version, shards):
    flow = Flow(
        name='test-flow-scale',
        port_expose=9090,
        infrastructure='K8S',
        protocol='http',
        timeout_ready=12000,
        k8s_namespace='test-flow-scale-ns',
    ).add(
        name='test_executor',
        shards=shards,
        replicas=DEFAULT_REPLICAS,
        timeout_ready=12000,
    )
    # with flow as f:
    #     from jina.peapods.pods.k8slib.kubernetes_client import K8sClients
    #
    #     deployment = K8sClients().apps_v1.read_namespaced_deployment(
    #         name='test-executor', namespace='test-flow-scale-ns'
    #     )
    #     replica = deployment.status.replicas
    #
    #     assert replica == DEFAULT_REPLICAS
    #
    #     f.scale(pod_name='test_executor', replicas=3)  # scale up to 3
    #
    #     deployment = K8sClients().apps_v1.read_namespaced_deployment(
    #         name='test-executor', namespace='test-flow-scale-ns'
    #     )
    #     replica = deployment.status.replicas
    #
    #     assert replica == 3
    #
    #     f.scale(pod_name='test_executor', replicas=1)  # scale down to 1
    #
    #     deployment = K8sClients().apps_v1.read_namespaced_deployment(
    #         name='test-executor', namespace='test-flow-scale-ns'
    #     )
    #     replica = deployment.status.replicas
    #
    #     assert replica == 1


# def test_k8s_scale_fail(
#     k8s_cluster,
#     load_images_in_kind,
#     set_test_pip_version,
# ):
#     flow = Flow(
#         name='test-flow-scale',
#         port_expose=9090,
#         infrastructure='K8S',
#         protocol='http',
#         timeout_ready=12000,
#         k8s_namespace='test-flow-scale-ns',
#     ).add(
#         name='test_executor',
#         shards=1,
#         replicas=DEFAULT_REPLICAS,
#         timeout_ready=0,
#     )
#     with flow as f:
#         from jina.peapods.pods.k8slib.kubernetes_client import K8sClients
#
#         deployment = K8sClients().apps_v1.read_namespaced_deployment(
#             name='test-executor', namespace='test-flow-scale-ns'
#         )
#         replica = deployment.status.replicas
#         assert replica == DEFAULT_REPLICAS
#
#         f.scale(pod_name='test_executor', replicas=3)
#         deployment = K8sClients().apps_v1.read_namespaced_deployment(
#             name='test-executor', namespace='test-flow-scale-ns'
#         )
#         replica = deployment.status.replicas
#         assert replica == 3
