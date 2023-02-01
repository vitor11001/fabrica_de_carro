class Mecanica:
    def __init__(self) -> None:
        self.consumo = str()
        self.cambio = str()
        self.qtd_marchas = int()
        self.tipo_injecao = str()
        self.amortecedor = str()
        self.radiador_tubular = bool()
        self.freios_abs = bool()
        self.turbo = bool()
        
    def write_consup(self, consumo: str) -> None:
        self.consumo = consumo
        
    def write_exchange(self, cambio: str) -> None:
        self.cambio = cambio
    
    def write_amount_gears(self, qtd_marchas: int) -> None:
        self.qtd_marchas = qtd_marchas
    
    def write_type_injection(self, tipo_injecao: str) -> None:
        self.tipo_injecao = tipo_injecao
    
    def write_absorver(self, amortecedor: str) -> None:
        self.amortecedor = amortecedor
    
    def write_tub_radiator(self, radiador_tubular: bool) -> None:
        self.radiador_tubular = radiador_tubular
    
    def write_brakes_abs(self, freios_abs: bool) -> None:
        self.freios_abs = freios_abs
    
    def write_turbo(self, turbo: bool) -> None:
        self.turbo = turbo
    
    def read_consup(self) -> str:
        return self.consumo
    
    def read_exchange(self) -> str:
        return self.cambio
    
    def read_amount_gears(self) -> int:
        return self.qtd_marchas
    
    def read_type_injection(self) -> str:
        return self.tipo_injecao
    
    def read_absorver(self) -> str:
        return self.amortecedor
    
    def read_tub_radiator(self) -> bool:
        return self.radiador_tubular
    
    def read_brakes_abs(self) -> bool:
        return self.freios_abs
    
    def read_turbo(self) -> bool:
        return self.turbo
    
    def read_all_mechanics(self) -> dict:
        dicio = {'consumo': self.consumo, 'cambio': self.cambio, 'qtd_marchas': self.qtd_marchas, 'tipo_injecao': self.tipo_injecao,
                 'amortecedor': self.amortecedor, 'radiador_tubular': self.radiador_tubular, 'freios_abs': self.freios_abs, 'turbo': self.turbo}
        return dicio