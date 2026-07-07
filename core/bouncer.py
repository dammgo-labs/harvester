class Bouncer:
    def __init__(self, bullshit_terms, deep_keywords):
        self.bullshit_terms = [term.lower() for term in bullshit_terms]
        # Normalizamos comillas para procesar lógicas AND muy básicas
        self.deep_keywords = [kw.lower().replace('"', '') for kw in deep_keywords]

    def passes_filter(self, text: str) -> bool:
        if not text:
            return False
            
        text_lower = text.lower()
        
        # 1. Filtro Negativo (El Cadenero): Si hay basura, se desecha inmediatamente.
        for bs in self.bullshit_terms:
            if bs in text_lower:
                return False
                
        # 2. Filtro Positivo: Debe contener al menos uno de los bloques de palabras clave.
        passed_positive = False
        for kw_group in self.deep_keywords:
            # Soportar un cruce AND básico (ej. "Hemi-Sync AND biological oscillator")
            parts = [p.strip() for p in kw_group.split(' and ')]
            if all(part in text_lower for part in parts):
                passed_positive = True
                break
                
        return passed_positive
