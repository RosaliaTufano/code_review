import opennmt


class MyCustomTransformer(opennmt.models.Transformer):
    def __init__(self):
        super().__init__(
            source_inputter=opennmt.inputters.WordEmbedder(256),
            target_inputter=opennmt.inputters.WordEmbedder(256),
            num_layers=[1, 3],
            num_units=256,
            num_heads=8,
            ffn_inner_dim=256,
            dropout=0.2798,
            attention_dropout=0.1873,
            ffn_dropout=0.2134)


model = MyCustomTransformer
