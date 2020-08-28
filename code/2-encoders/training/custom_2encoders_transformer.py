import opennmt


class MyCustomTransformer(opennmt.models.Transformer):
    def __init__(self):
        super().__init__(
            source_inputter=opennmt.inputters.ParallelInputter(
                [opennmt.inputters.WordEmbedder(embedding_size=512),
                 opennmt.inputters.WordEmbedder(embedding_size=512)]),
            target_inputter=opennmt.inputters.WordEmbedder(embedding_size=512),
            num_layers=[2, 4],
            num_units=512,
            num_heads=4,
            ffn_inner_dim=512,
            dropout=0.1168,
            attention_dropout=0.1794,
            ffn_dropout=0.2809,
            share_encoders=True)


model = MyCustomTransformer
