typedef enum logic [3:0] {
    ALU_ADD  = 4'b0000,
    ALU_SUB  = 4'b0001,
    ALU_AND  = 4'b0010,
    ALU_OR   = 4'b0011,
    ALU_XOR  = 4'b0100,
    ALU_SLL  = 4'b0101,
    ALU_SRL  = 4'b0110,
    ALU_SRA  = 4'b0111,
    ALU_SLT  = 4'b1000,
    ALU_SLTU = 4'b1001
} alu_op_t;

module alu (
    input  logic [31:0] a,
    input  logic [31:0] b,
    input  alu_op_t     op,

    output logic [31:0] y
);
    always_comb begin
        case (op)
            ALU_ADD:  y = a + b;
            ALU_SUB:  y = a - b;
            ALU_AND:  y = a & b;
            ALU_OR:   y = a | b;
            ALU_XOR:  y = a ^ b;
            ALU_SLL:  y = a <<  b[4:0];
            ALU_SRL:  y = a >> b[4:0];
            ALU_SRA:  y = $signed(a) >>> b[4:0];
            ALU_SLT:  y = {31'b0, ($signed(a) < $signed(b))};
            ALU_SLTU: y = {31'b0, (a < b)};
            default:  y = 32'b0;
        endcase
    end
endmodule