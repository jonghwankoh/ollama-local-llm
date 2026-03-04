# Local LLM Hub

다양한 로컬 LLM 모델을 Ollama 엔진을 통해 통합 관리하고 테스트할 수 있는 리포지토리입니다.

## 📁 디렉토리 구조

- `engines/`: 각 LLM 엔진별 설정 파일 (예: Ollama Modelfile)
- `profiles/`: 모델 실행을 위한 YAML 프로필 설정
- `models/`: 로컬 모델 파일 (GGUF, Safetensors 등) 위치
- `scripts/`: 테스트 및 유틸리티 스크립트
- `local_llm.py`: 메인 모델 실행 관리자

## 🚀 빠른 시작

### 1. 환경 설정
Python이 설치되어 있어야 하며, 필요한 라이브러리를 설치합니다.
```bash
pip install -r requirements.txt
```

### 2. 모델 실행
`run.bat` 파일에 프로필 이름을 인자로 주어 실행합니다.
```bash
run.bat qwen2.5-3b-instruct-q8_0
```
*(기본적으로 `profiles/qwen2.5-3b-instruct-q8_0.yaml` 파일을 찾아 실행합니다)*

### 3. API 테스트
모델이 실행 중일 때, 별도의 터미널에서 테스트 스크립트를 실행합니다.
```bash
python scripts/client_test.py --profile qwen2.5-3b-instruct-q8_0
```

## 🛠️ 새로운 모델 추가하기

### Ollama 모델 추가
1.  `engines/ollama/` 폴더에 새로운 `Modelfile`을 작성합니다.
2.  `profiles/` 폴더에 해당 모델을 위한 `.yaml` 파일을 생성합니다.
    ```yaml
    name: "my-new-model"
    engine: "ollama"
    model_name: "my-model-local"
    modelfile: "engines/ollama/MyNewModelfile"
    api_base: "http://localhost:11434/v1"
    ```
3.  `run.bat my-new-model`로 실행합니다.

---

---

## 📋 기존 Ollama 사용법 참고

- **Ollama 설치**: [ollama.com](https://ollama.com)에서 설치
- **GGUF 모델**: `models/` 폴더에 `.gguf` 파일을 위치시킨 후 `Modelfile`에서 경로를 참조하세요.
