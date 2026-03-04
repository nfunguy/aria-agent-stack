package aria

default allow = true

deny[msg] {
    input.variance < -100
    msg := "Variance exceeds allowable threshold"
}
