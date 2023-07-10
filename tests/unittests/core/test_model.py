import torch

from superduperdb.models.torch.wrapper import TorchModel
from superduperdb.datalayer.mongodb.query import Collection


def test_predict(random_data, float_tensors_32):
    encoder = random_data.types['torch.float32[32]']

    m = TorchModel(
        identifier='my-model',
        object=torch.nn.Linear(32, 7),
        encoder=encoder,
    )

    X = [r['x'] for r in random_data.execute(Collection(name='documents').find())]

    out = m.predict(X=X, remote=False)

    assert len(out) == len(X)

    m.predict(
        X='x',
        db=random_data,
        select=Collection(name='documents').find(),
        remote=False,
    )