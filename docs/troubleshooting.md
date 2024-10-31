# 문제 해결 가이드

## SSL 인증서 관련 문제

### 문제 상황
pip install 시 다음과 같은 SSL 인증서 오류 발생:

WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1131)'))


### 해결 방법
`--trusted-host` 옵션을 사용하여 설치:
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org [패키지명]


# konlpy 설치
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org konlpy

# jpype1 설치
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org jpype1


참고

이 방법은 SSL 인증서 문제를 우회하는 임시 해결책입니다
기업 환경에서 자주 발생하는 문제입니다
보다 근본적인 해결을 위해서는 시스템 관리자와 상담이 필요할 수 있습니다
